import {Ref} from 'vue'
import { NonReactiveOrderedPizzas} from './pizza'

export interface ClientData{
    client_data: { [data: string]: Ref<String>}
}

export interface ClientDataMeta{
    client_data_meta: { [data: string]: {type: string, placeholder: string}}
}

export interface FinalOrder{
    name: string,
    surname: string,
    email: string,
    postal_code: string,
    address: string,
    pizzas: NonReactiveOrderedPizzas
}