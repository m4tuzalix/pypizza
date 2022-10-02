<template>
    <div class='w-50'>
        <div class='d-flex flex-row p-1' v-for='order of props.final_orders' :key='order'>
            <div class='d-flex w-100'>
                <span >{{order.pizza.name}}</span><br>
                <span>({{order.size}})</span>
            </div>
            <div>
                <span>x{{order.amount}}</span>
            </div>
        </div>
        <div class='d-flex flex-row p-1 mt-5'>
            <div class="d-flex w-100">Total:</div>
            <div>
                <span>${{props.order_value}}</span>
            </div>
        </div>
    </div>
</template>
    
<script lang="ts">
import { defineComponent, ref, onMounted, PropType} from 'vue'
import { NonReactiveOrderedPizza} from '@/interfaces/pizza'
export default defineComponent({
    props:{
        final_orders:{
            type: Object as PropType<NonReactiveOrderedPizza>
        },
        order_value:{
            type: Object as PropType<number>,
            required: true
        }
    },
    setup(props){
        return{props}
    }
})
</script>
    