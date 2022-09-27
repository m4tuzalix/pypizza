import { NonReactiveOrderedPizza, PizzaSize } from "./pizza"

export interface PizzaOrder{
    orders: { [pizza_name: string]: PizzaOrderDetails}
}

export interface PizzaOrderDetails{
    order: {[size: string] : NonReactiveOrderedPizza}
}

export interface State{
    orders: PizzaOrder,
}