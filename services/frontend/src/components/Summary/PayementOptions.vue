<template>
    <div>payement</div>
</template>
    
<script lang="ts">
import { defineComponent, ref, onMounted, PropType} from 'vue'
import {ClientData} from '@/interfaces/summary_interface'
export default defineComponent({
    props:{
        client_data:{
            type: Object as PropType<ClientData>,
            required: true
        }
    },
    setup(props){
    }
})
</script>
    