<template>
    <div class="modal fade" id="cartModal" tabindex="-1" aria-labelledby="cartModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="cartModalLabel">Cart</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body container">
                    <div class='d-flex flex-row p-1' v-for='order of STORE.state.final_orders'>
                        <div class='col'>
                            <span>{{order.pizza.name}}</span><br>
                            <span class='ml-2'>({{order.size}})</span>
                        </div>
                        <div class='col'>
                            <span>x{{order.amount}}</span>
                        </div>
                        <div class='col'>
                            <b-button variant="danger" @click='func_delete_from_order(order)' :data-bs-dismiss="STORE.getters.last_order ? 'modal' : 'false'">Delete</b-button>
                        </div>
                    </div>
                </div>
                <div class="d-flex justify-content-center">
                    <b-badge class='mr-5' variant="success">Total: {{STORE.state.order_value}}$</b-badge>
                </div>
                <div class="modal-footer">
                    <b-button data-bs-dismiss="modal">close</b-button>
                    <b-button href='/summary'>buy</b-button>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script lang="ts">
import { defineComponent, ref, onMounted, PropType} from 'vue'
import { NonReactiveOrderedPizza, ReactiveOrderedPizza } from '@/interfaces/pizza'
import { useStore } from 'vuex'
import { key } from '@/store'
import router from '@/router'
import {api} from "@/api.js"
export default defineComponent({
    setup(){
        const STORE = useStore(key)

        const func_delete_from_order = (order: ReactiveOrderedPizza)=>{
            STORE.dispatch('delete_single_item', order)
            if(!STORE.getters.empty_cart){STORE.dispatch('update_final_orders')}
        }
        return {STORE, func_delete_from_order}
    }
})
</script>
    
<style scoped>
    .btn-close {display: none;}
</style>