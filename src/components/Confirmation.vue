<template>
  <div>
    <b-alert ref="hider" variant="success" show>
             {{ message }}
             <b-button type="hider" class="close" data-dismiss="alert"
             aria-label="Close"
             @click="hider()">
               <span aria-hidden="true">x</span></b-button>
    </b-alert>
  </div>
</template>

<script>
export default {
  name: 'Confirmation',
  props: ['message'],
  methods: {
    hider() {
      // console.log(this.$refs.hider);
      this.$refs.hider.show = false;
    },
  },

};
</script>
