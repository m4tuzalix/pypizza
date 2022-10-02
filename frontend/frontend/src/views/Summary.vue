<template>
  <div>
    <OrderDetails :final_orders='props.final_orders' :order_value='props.order_value'/>
    <ClientDetails :client_data='client_data' :client_data_meta='_client_data_meta'/>
    <PayementOptions/>
    <button @click='SentOrder'>Order</button>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, PropType} from 'vue'
import {NonReactiveOrderedPizzas} from '@/interfaces/pizza';
import {FinalOrder} from '@/interfaces/summary_interface';
import OrderDetails from '@/components/Summary/OrderDetails.vue'
import PayementOptions from '@/components/Summary/PayementOptions.vue'
import ClientDetails from '@/components/Summary/ClientDetails.vue'
import {api} from "@/api.js"
export default defineComponent({
    components:{
        OrderDetails, 
        ClientDetails,
        PayementOptions
    },
    props:{
        final_orders:{
            type: Object as PropType<NonReactiveOrderedPizza>,
            required: true
        },
        order_value:{
            type: Object as PropType<number>,
            required: true
        }
    },
  setup(props){
    const CLIENT_NAME = ref('')
    const CLIENT_SURNAME = ref('')
    const CLIENT_PHONE = ref('')
    const CLIENT_EMAIL = ref('')
    const CLIENT_POSTAL_CODE = ref('')
    const CLIENT_ADDRESS = ref('')

    const client_data={
        name: CLIENT_NAME,
        surname: CLIENT_SURNAME,
        email: CLIENT_EMAIL,
        phone: CLIENT_PHONE,
        postal_code: CLIENT_POSTAL_CODE,
        address: CLIENT_ADDRESS
    }
    const _client_data_meta = {
        name: {
            type: 'text',
            placeholder: 'name'
        },
        surname: {
            type: 'text',
            placeholder: 'surname'
        },
        phone: {
            type: 'text',
            placeholder: 'phone'
        },
        email: {
            type: 'email',
            placeholder: 'email'
        },
        postal_code: {
            type: 'text',
            placeholder: 'postalcode'
        },
        address: {
            type: 'text',
            placeholder: 'address'
        }
    }

    const _updateOrderStatus = async (order_id: number)=>{
        const verification_status = 1
        await api.post('order/update_status/', {order_id: order_id, status: verification_status})
        .catch(response =>{
            console.log('sth wrong with status update')
        })
    }

    const SentOrder = async ()=>{
        const data: FinalOrder = Object.fromEntries(
            Object.entries(client_data).map(
                ([ key, val ]) => [ key, val.value])
            )  
        await api.post('order/create_order/', {...data, pizzas:props.final_orders})
        .then(response => {
            const order_id = response.data.id
            _updateOrderStatus(order_id)
        })
        .catch(response => {
            console.log(response)
        })
    }
    return{props, client_data, _client_data_meta, SentOrder}
  }
})
</script>