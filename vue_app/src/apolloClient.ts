import {
  ApolloClient,
  ApolloLink,
  FetchResult,
  HttpLink,
  InMemoryCache,
  Observable,
  Operation,
  split,
} from "@apollo/client/core";
import { getMainDefinition } from "@apollo/client/utilities";
import { GraphQLError, print } from "graphql";
import { Client, ClientOptions, createClient } from 'graphql-ws';

const cache = new InMemoryCache();

const httpLink = new HttpLink({
  uri: window.location.origin + "/api/",
});


class WebSocketLink extends ApolloLink {
  public client: Client;

  constructor(options: ClientOptions) {
    super();
    this.client = createClient(options);
  }

  public request(operation: Operation): Observable<FetchResult> {
    return new Observable((sink) => {
      return this.client.subscribe<FetchResult>(
        { ...operation, query: print(operation.query) },
        {
          next: sink.next.bind(sink),
          complete: sink.complete.bind(sink),
          error: (err) => {
            if (err instanceof Error) {
              sink.error(err);
            } else if (err instanceof CloseEvent) {
              sink.error(
                new Error(
                  `Socket closed with event ${err.code}` + err.reason
                    ? `: ${err.reason}` // reason will be available on clean closes
                    : '',
                ),
              );
            } else {
              sink.error(
                new Error(
                  (err as GraphQLError[])
                    .map(({ message }) => message)
                    .join(', '),
                ),
              );
            }
          },
        },
      );
    });
  }
}

const wsLink = new WebSocketLink({
  url: `${window.location.protocol === "http:" ? "ws" : "wss"}://${
    window.location.host
  }/graphqlws/`,
});

wsLink.client.on("closed", (e) => {
  //@ts-ignore
  if (e.code === 4499) {
    console.log("Websocket - Disposed");
    wsLink.client.dispose();
  } else {
    //@ts-ignore
    console.log("Websocket - Closed", e.code);
  }
});

const usedApolloLink = split(
  // split based on operation type
  ({ query }) => {
    const mainDefinition = getMainDefinition(query);
    return (
      mainDefinition.kind === "OperationDefinition" &&
      mainDefinition.operation === "subscription"
    );
  },
  wsLink,
  httpLink
);

const link = ApolloLink.from([usedApolloLink]);

const apolloClient = new ApolloClient({
  link,
  cache,
  defaultOptions: {
    watchQuery: {
      nextFetchPolicy(lastFetchPolicy) {
        if (
          lastFetchPolicy === "cache-and-network" ||
          lastFetchPolicy === "network-only"
        ) {
          return "cache-first";
        }
        return lastFetchPolicy;
      },
    },
  },
  resolvers: {},
});

export default apolloClient;
