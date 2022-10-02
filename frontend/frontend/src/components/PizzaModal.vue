<template>
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">{{props.pizza.name}}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body container">
        <div class="d-inline-block p-2">
          amount: {{amount}}
        </div>
        <div class="d-inline-block p-3">
          <button type="button" class="btn btn-primary btn-sm" @click='amount++'>+</button>
          <div class='d-inline-block p-1'></div>
          <button :disabled='amount < 2' type="button" class="btn btn-primary btn-sm" @click='amount--'> -</button>
        </div>
        <br>
        <div class='d-inline-block p-1' v-for='size of _pizza_size'>
            <b-button @click='size_choice = size' class="btn d-inline p-2" :variant='size_choice == size ? "success":"info"'>{{size}}</b-button>
        </div>
      </div>
      <div class="modal-footer">
        <button @click='size_choice = props.default_size' type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button @click='func_make_order' type="button" class="btn btn-primary" data-bs-dismiss="modal">Add to cart</button>
      </div>
    </div>
  </div>
</div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, PropType} from 'vue'
import {PizzaInterface, ReactiveOrderedPizza, PizzaSize} from '@/interfaces/pizza'
import { useStore } from 'vuex'
import { key } from '@/store'

export default defineComponent({
    props:{
      pizza: {
        type: Object as PropType<PizzaInterface>,
        required: true
      },
      default_size: {
        type: String,
        required: true,
      }
    },
    setup(props){
        const STORE = useStore(key)
        const _pizza_size = [PizzaSize.SMALL, PizzaSize.MEDIUM, PizzaSize.BIG]

        const amount = ref(1)
        const size_choice = ref(PizzaSize.MEDIUM)

        const _set_default_size = ()=>{
          size_choice.value = PizzaSize.MEDIUM
        }

        const _set_default_amount = ()=>{
          amount.value = 1
        }

        const func_make_order = ()=>{
            const order: ReactiveOrderedPizza = {
            pizza: props.pizza,
            amount: amount,
            size: size_choice
          }
          STORE.dispatch('make_order', order)
          STORE.dispatch('update_final_orders')

          _set_default_size()
          _set_default_amount()
        }

        return{
          _pizza_size, size_choice, amount, STORE, props, func_make_order
        }
    }
})
</script>

<style scoped>
  .btn-close {display: none;}
</style>