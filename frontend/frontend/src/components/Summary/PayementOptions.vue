<template>
    <div>payement</div>
</template>
    
<script lang="ts">
import { defineComponent, ref, onMounted, PropType} from 'vue'
import {CLientData} from '@/interfaces/summary_interface.ts'
export default defineComponent({
    props:{
        client_data:{
            type: Object as PropType<CLientData>,
            required: true
        }
    },
    setup(props){
    }
})
</script>
    