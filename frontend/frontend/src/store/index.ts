import { createStore, Store} from 'vuex';
import { InjectionKey, Ref, PropType } from 'vue';
import {PizzaOrder, PizzaOrderDetails, State} from '../interfaces/vuex_interfaces'
import { ReactiveOrderedPizza, NonReactiveOrderedPizza, PizzaInterface, PizzaSize } from '@/interfaces/pizza';
import createPersistedState from "vuex-persistedstate";

export const key: InjectionKey<Store<State>> = Symbol()

export const store = createStore<State>({
  plugins: [createPersistedState()],
  state(){
    return{
      orders: <PizzaOrder>{},
    }
  },
  getters: {
    get_orders(state: State){
      return state.orders
    },

  },
  mutations: {
    add_pizza_to_order(state: State, ordered_pizza: NonReactiveOrderedPizza){
      const [_pizzaName, _pizzaSize, _amount] = [ordered_pizza.pizza.name, ordered_pizza.size, ordered_pizza.amount]
      const pizzaOrder = state.orders[_pizzaName]

      if(!pizzaOrder){state.orders[_pizzaName] = <PizzaOrderDetails>{}}

      state.orders[_pizzaName][_pizzaSize] = ordered_pizza
    },
  },
  actions: {
    make_order(context, OrderedPizza: ReactiveOrderedPizza){
      const _parse_ref_to_obj = (object: Ref<number> | number | string | Ref<PizzaSize>)=>{
        return JSON.parse(JSON.stringify(object))._value
      }
      const _OrderedPizza = {
        pizza: OrderedPizza.pizza,
        size: _parse_ref_to_obj(OrderedPizza.size),
        amount: _parse_ref_to_obj(OrderedPizza.amount),
      }
      context.commit('add_pizza_to_order', _OrderedPizza)
    },
    finalize_order(context): Array<NonReactiveOrderedPizza>{
      const _complete_order: Array<Array<NonReactiveOrderedPizza>> = Array.from(Object.values(context.state.orders), _order=>{
        const _pizzas: Array<NonReactiveOrderedPizza> = Object.values(JSON.parse(JSON.stringify(_order)))
        return _pizzas
      })
      return _complete_order.flatMap(order => order)
    },
    count_order_price(context, orders: Array<NonReactiveOrderedPizza>): number{
      const _prices: Array<number> = Array.from(orders, order =>{
        return order.pizza.price * order.amount
      })
      return _prices.reduce((previous, actual) =>{
        return previous + actual
      })
    }
  },
  modules: {
  },
});
