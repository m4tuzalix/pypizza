<template>
    <div>
        <div class="mt-5 mb-2">
            <span>
                Delivery details:
            </span>
        </div>
        <div class='w-50'>
            <b-form-input v-for='key in Object.keys(props.client_data)' 
                class="mb-1"
                :key='key'
                :placeholder="'Enter your '+client_data_meta[key].placeholder"
                :type='client_data_meta[key].type'
                v-model='client_data[key].value'>
            </b-form-input>
        </div>
    </div>
</template>
    
<script lang="ts">
import { defineComponent, ref, onMounted, PropType} from 'vue'
import {ClientData, ClientDataMeta} from '@/interfaces/summary_interface'
export default defineComponent({
    props:{
        client_data:{
            type: Object as PropType<ClientData>,
            required: true
        },
        client_data_meta:{
            type: Object as PropType<ClientDataMeta>,
            required: true
        }
    },
    setup(props){
        return{props}
    }
})
</script>
    