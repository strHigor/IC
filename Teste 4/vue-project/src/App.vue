<script>
import Buscas from './services/buscas.js'

export default {
  data() {
    return {
      dados: [
        {
          registro_ans: "",
          cnpj: "",
          razão_social: "",
          nome_fantasia: "",
          modalidade: "",
          logradouro: "",
          número: "",
          complemento: "",
          bairro: "",
          cidade: "",
          uf: "",
          cep: "",
          ddd: "",
          telefone: "",
          fax: "",
          endereço_eletrônico: "",
          representante: "",
          cargo_representante: "",
          data_registro_ans: ""
        }
      ],
      displayTable: "display",
      input: null
    }
  },
  methods: {
    procurar(value) {
      if (value.length > 2) {
        Buscas.listar(value).then(resposta => {
          if (resposta.status == 200) {
            this.dados = resposta.data
          }
        })
      } else {
        alert('Valor minimo de caracteres: 3')
      }
    }
  }
}
</script>

<template>
  <div id="app">
    <div id="inputs">
      <label for="buscar"></label>
      <input type="text" minlength="3" id="buscar" name="buscar" v-model="input" placeholder="Buscar Operadora">
      <input v-on:click="procurar(this.input)" type="submit" class="btn" value="Procurar">
    </div>

    <!-- cria a tabela com os valores -->
    <div :style="{ display: displayTable }">
      <table>
        <tr>
          <th> Registro ANS </th>
          <th> CNPJ </th>
          <th> Razão Social </th>
          <th> Nome Fantasia </th>
          <th> Modalidade </th>
          <th> Logradouro </th>
          <th> Número </th>
          <th> Complemento </th>
          <th> Bairro </th>
          <th> Cidade </th>
          <th> UF </th>
          <th> CEP </th>
          <th> DDD </th>
          <th> Telefone </th>
          <th> Fax </th>
          <th> Email </th>
          <th> Representante </th>
          <th> Cargo Representante </th>
          <th> Data de Registro ANS </th>
        </tr>
        <tr v-for="arr in dados">
          <td>{{ arr.registro_ans }}</td>
          <td>{{ arr.cnpj }}</td>
          <td>{{ arr.razão_social }}</td>
          <td>{{ arr.nome_fantasia }}</td>
          <td>{{ arr.modalidade }}</td>
          <td>{{ arr.logradouro }}</td>
          <td>{{ arr.número }}</td>
          <td>{{ arr.complemento }}</td>
          <td>{{ arr.bairro }}</td>
          <td>{{ arr.cidade }}</td>
          <td>{{ arr.uf }}</td>
          <td>{{ arr.cep }}</td>
          <td>{{ arr.ddd }}</td>
          <td>{{ arr.telefone }}</td>
          <td>{{ arr.fax }}</td>
          <td>{{ arr.endereço_eletrônico }}</td>
          <td>{{ arr.representante }}</td>
          <td>{{ arr.cargo_representante }}</td>
          <td>{{ arr.data_registro_ans }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<style>

</style>
