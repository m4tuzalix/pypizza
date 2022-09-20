<template>
<div><Pizzas/></div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted} from 'vue'
import Pizzas from '@/components/Pizzas.vue'
export default defineComponent({
  components:{
    Pizzas
  },

  setup(){

    const cart = ref({})
  }
})
</script>