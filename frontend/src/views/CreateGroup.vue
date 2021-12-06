<template>
  <div>
    <p>test</p>
    <form @submit.prevent="create_join_group">
      <p>Create Group</p>
      <h1>currentGroupID : {{ this.$store.state.currentGroupID }}</h1>
      <div> {{ this.$store.state.Group }} </div>
      <!-- <h1>currentGroupName : {{ this.$store.state.Group[this.$store.state.currentGroupID]["name"] }}</h1> -->
      <textarea
        v-model="newGroupName"
        class="form-control"
        placeholder=""
        rows="1"
      ></textarea>
      <Button>
        Create Group
      </Button>
    </form>
  </div>
</template>

<script>
import Button from '../components/Atoms/Button.vue'
export default {
	name: "CreateGroup",
	components: {
		  Button
	},
	data() {
		  return {
			    newGroupName: null
		  }
	},
	methods: {
		  create_join_group() {
			    this.$store.dispatch('getCreateGroup', {newGroupName: this.newGroupName})
		  }
	},
}
</script>

<style>

</style>