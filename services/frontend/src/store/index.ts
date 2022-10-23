import { createStore, Store} from 'vuex';
import { InjectionKey, Ref} from 'vue';
import {PizzaOrder, PizzaOrderDetails, State} from '../interfaces/vuex_interfaces'
import { ReactiveOrderedPizza, NonReactiveOrderedPizza, PizzaSize, NonReactiveOrderedPizzas} from '@/interfaces/pizza';
import createPersistedState from "vuex-persistedstate";

export const key: InjectionKey<Store<State>> = Symbol()

export const store = createStore<State>({
  plugins: [createPersistedState()],
  state(){
    return{
      orders: <PizzaOrder>{},
      final_orders: <NonReactiveOrderedPizzas>{},
      order_value: 0
    }
  },
  getters: {
    get_orders(state: State): PizzaOrder{
      return state.orders
    },
    empty_cart(state: State): boolean{
      return Object.keys(state.orders).length === 0
    },
    last_order(state: State): boolean{
      return state.final_orders.length === 1
    }

  },
  mutations: {
    add_pizza_to_order(state: State, ordered_pizza: NonReactiveOrderedPizza): void{
      // adds new order to global orders
      const [_pizzaName, _pizzaSize, _amount] : [string, PizzaSize, number] = [ordered_pizza.pizza.name, ordered_pizza.size, ordered_pizza.amount]
      const pizzaOrder: PizzaOrder = state.orders[_pizzaName]

      if(!pizzaOrder){state.orders[_pizzaName] = <PizzaOrderDetails>{}}

      if(state.orders[_pizzaName][_pizzaSize]){state.orders[_pizzaName][_pizzaSize].amount += _amount}
      else{state.orders[_pizzaName][_pizzaSize] = ordered_pizza}
    },
    remove_order(state: State, order: ReactiveOrderedPizza):  void{
      const [_pizzaName, _pizzaSize]: [string, Ref<PizzaSize>] = [order.pizza.name, order.size]
      delete state.orders[_pizzaName][_pizzaSize]
      if(Object.keys(state.orders[_pizzaName]).length === 0){delete state.orders[_pizzaName]}
    },
    set_final_orders(state: State, orders: NonReactiveOrderedPizzas): void{
      state.final_orders = orders
    },
    calc_final_price(state: State): void{
      const _prices: number = Array.from(state.final_orders, order =>{
        return order.pizza.price * order.amount
      }).reduce((previous: number, actual: number) => {return previous + actual})
      state.order_value = _prices
    }
  },
  actions: {
    make_order(context, OrderedPizza: ReactiveOrderedPizza): void{
      // Parses order to nonreactive state and passes it to mutations
      const _parse_ref_to_obj = (object: Ref<any> | any)=>{
        return JSON.parse(JSON.stringify(object))._value
      }
      const _OrderedPizza: NonReactiveOrderedPizza = {
        pizza: OrderedPizza.pizza,
        size: _parse_ref_to_obj(OrderedPizza.size),
        amount: _parse_ref_to_obj(OrderedPizza.amount),
      }
      context.commit('add_pizza_to_order', _OrderedPizza)
    },
    update_final_orders(context): void{
      // Creates proper format for backend [{order}, {order}, {order}] etc.
      const complete_order: NonReactiveOrderedPizzas = Array.from(Object.values(context.state.orders), _order=>{
        const _pizzas: NonReactiveOrderedPizzas = Object.values(_order)
        return _pizzas
      }).flatMap(order => order)
      context.commit('set_final_orders', complete_order)
      context.commit('calc_final_price')
    },
    delete_single_item(context, item: ReactiveOrderedPizza): void{
      context.commit('remove_order', item)
    }
  },
  modules: {
  },
});
