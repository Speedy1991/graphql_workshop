<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import { defineComponent } from '@vue/composition-api';
import { useQuery } from '@vue/apollo-composable';
import gql from 'graphql-tag';

const ProfessorQuery = gql`
  query ProfessorQuery {
    professors {
      id
      projects {
        id
        students {
          id
          name
          age
        }
        __typename
        ... on ResearchProjectType {
          supervisor
        }
      }
    }
  }
`;

export default defineComponent({
  name: 'App',
  components: {
    HelloWorld,
  },
  setup() {
    const { result, loading } = useQuery(ProfessorQuery);
    console.log(loading, result);
    return {};
  },
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
