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
          <button class="btn btn-primary btn-sm" type="submit">Add</button>
        </div>
      </div>
  </div>
</template>

<script>
import {api} from "@/api.js"
import { defineComponent, ref, onMounted } from 'vue'

export default defineComponent({
  setup(){

    const pizzas = ref([])

    onMounted(async ()=>{
      await api.get('pizza/pizzas/')
      .then(response=>{
        pizzas.value = response.data
      })
    })
    return{
      pizzas
    }
  }
})
</script>