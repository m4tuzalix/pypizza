<template>
  <div>
  <div class="d-flex justify-content-end mb-3">
    <b-button :disabled='STORE.getters.empty_cart' variant='danger' data-bs-toggle="modal" data-bs-target="#cartModal">Cart</b-button>
  </div>
    <Cart/>
    <Pizzas/>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted} from 'vue'
import Pizzas from '@/components/Pizzas.vue'
import Cart from '@/components/Cart.vue'
import { useStore } from 'vuex'
import { key } from '@/store'
export default defineComponent({
  components:{
    Pizzas,
    Cart
  },
  setup(){
    const STORE = useStore(key)
    return{STORE}
  }
})
</script>