import {Ref} from 'vue'

export enum PizzaSize{
    SMALL = 'small',
    MEDIUM = 'medium',
    BIG = 'big'
}

export interface PizzaInterface{
    name: string,
    ingredients: Array<string>,
    price: number
}

export interface ReactiveOrderedPizza{
    pizza: PizzaInterface,
    size: Ref<PizzaSize>,
    amount: Ref<number>
}

export interface NonReactiveOrderedPizza{
    pizza: PizzaInterface,
    size: PizzaSize,
    amount: number
}
