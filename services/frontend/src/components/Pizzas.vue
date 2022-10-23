<template>
  <div>
      <div class="row mb-2 border-top border-bottom" v-for="pizza in pizzas" :key="pizza">
        <div class="col-sm">
          <img alt="Vue logo" src="../assets/logo.png" style="height: 80px; width: 115px;">
        </div>
         <div class="col-6">
            <div class="row mt-4">
              <div class="col-3">
                <span class="badge bg-secondary">{{pizza.name}}</span>
              </div>
              <div class="col">
                {{(pizza.ingredients).join(", ")}}
              </div>
            </div>
          </div>
        <div class="col mt-4 d-flex justify-content-center">
          starting from: ${{pizza.price}}
        </div>
        <div class="col mt-4">
          <button type="button" class="btn btn-primary btn-sm" @click='selected_pizza = pizza' data-bs-toggle="modal" data-bs-target="#exampleModal">Add</button>
        </div>
      </div>
      <PizzaModal :pizza='selected_pizza' default_size='medium'/>
</div>
</template>

<script lang="ts">
import {api} from "@/api.js"
import {defineComponent, ref, onMounted, PropType} from 'vue'
import PizzaModal from '@/components/PizzaModal.vue'
import router from '@/router';

export default defineComponent({
  components:{
    PizzaModal
  },
  setup(){

    const pizzas = ref({})
    const selected_pizza = ref({})

    onMounted(async ()=>{
      await api.get('pizza/pizzas/')
      .then(response=>{
        pizzas.value = response.data
      })
      .catch(error =>{
        console.log(error)
        router.push('/')
      })
    })
    return{
      pizzas,
      selected_pizza,
    }
  }
})
</script>