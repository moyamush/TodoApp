<template>
  <button
    class="button-text btn btn-success my-3"
    @click="handleClick"
  >
    <slot />
  </button>
</template>

<script>
export default {
    name: 'Button',
    // props: {
    //     type: {
    //       type: String,
    //       default: 'button'
    //     }
    // },
    methods: {
        handleClick(ev) {
          this.$emit('click', ev)
        } 
    }    
}
</script>

<style>

</style>