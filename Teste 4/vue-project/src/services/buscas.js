import { http } from './config'

export default {
    listar:(value) => {
        return http.get('operadoras/' + value)
    }
}