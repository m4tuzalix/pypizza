<template>
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">{{props.pizza.name}}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div class="row">
          <div class="col">
            amount: {{amount}}
          </div>
          <div class="col">
            <button type="button" class="btn btn-primary btn-sm" @click='amount++'>+</button>
            <button :disabled='amount < 2' type="button" class="btn btn-primary btn-sm" @click='amount--'> -</button>
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Add to cart</button>
      </div>
    </div>
  </div>
</div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, PropType} from 'vue'
import {PizzaInterface} from '@/interfaces/pizza'

export default defineComponent({
    props:{
      pizza: {
        type: Object as PropType<PizzaInterface>,
        required: true
      }
    },
    setup(props){
        const amount = ref(1)
        return{
          amount, props
        }
    }
})
</script>