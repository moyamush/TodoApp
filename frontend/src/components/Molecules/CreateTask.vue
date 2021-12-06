<template>
	<div id="overlay">
    <div id="content">
      <button @click="clickEvent">close</button>
      <form @submit.prevent="createTask">
        <p>Create Task</p>
        <h1>currentGroupID : {{ this.$store.state.currentGroupID }}</h1>
        <textarea
          v-model="newTaskBody"
          class="form-control"
          placeholder="タスク名を入力"
          rows="10"
        ></textarea>
        <div>
          DeadLine : 
          <input v-model="deadline_at" type="datetime-local">
        </div>
        <button type="submit" class="button-text btn btn-success my-3">
            Create Task
        </button>
      </form>
    </div>
	</div>
</template>

<script>
export default {
    name: "CreateTask",
    data() {
        return {
            newTaskBody: null,
            deadline_at: null,
        }
    },
    methods :{
        clickEvent: function(){
            this.$emit('from-child')
        },
        createTask() {
            this.$store.dispatch('getCreateTask', {newTaskBody: this.newTaskBody, deadline_at: this.deadline_at})
            this.$store.dispatch('getCurrentGroupTasks')
            this.$emit('create')
        }
    }
}
</script>

<style>
#overlay {
  /*　要素を重ねた時の順番　*/
  z-index:1;

  /*　画面全体を覆う設定　*/
  position:fixed;
  top:0;
  left:0;
  width:100%;
  height:100%;
  background-color:rgba(0,0,0,0.5);

  /*　画面の中央に要素を表示させる設定　*/
  display: flex;
  align-items: center;
  justify-content: center;
}

#content{
  z-index:2;
  width:50%;
  padding: 1em;
  border-radius: 10px;
  background:#fff;
}

.button-text {
    color: white;
}


</style>