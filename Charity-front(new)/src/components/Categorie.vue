<script>
import axios from 'axios';
export default {
 data(){
   return {
    categorie: {
      libelle: ''
    },
    categories: []
  };
 },
  name: "Categories",
  mounted() {
    this.allCategorie();
  },
  methods:{
    async allCategorie(){
      await axios
          .get('http://127.0.0.1:5000/api/charity/listCategories')
          .then(value => {
            this.categories = value.data
            console.log(value.data)
          })
          .catch(error => {
            console.log(error)
          })
    },
    async addCategorie(){
     await axios
        .post("http://127.0.0.1:5000/api/charity/categories",this.categorie)
        .then(response=>{
          console.log("response",response.data);
          this.categorie={
            libelle:""
          }
          this.allCategorie();
        }).catch((error)=>{
          console.log(error)
     })
    },
    async deleteCategorie(cat){
      await axios.delete("http://127.0.0.1:5000/api/charity/delete/"+cat.id)
          .then(response=>{
            console.log("response",response.data);
            this.allCategorie();
          }).catch((error)=>{
            console.log(error)})
    },
    async showModal(cat){
      this.categorie = cat
      const modalDiv = document.getElementById('myModal');
      if(modalDiv!= null){
        modalDiv.style.display = 'block'
      }
    },
    async updateCategorie(){
      console.log('Catégorie update',this.categorie)
      await axios.put("http://127.0.0.1:5000/api/charity/update/"+this.categorie.id, this.categories)
               .then(response=>{
                    console.log("response",response.data);
                    this.allCategorie();
                    this.CloseModal()
               }).catch((error)=>{
                    console.log(error)})
    },
    CloseModal(){
    const modalDiv = document.getElementById('myModal');
    if(modalDiv!= null){
      modalDiv.style.display = 'none'
    }
  }
  },
  props: {}
}
</script>

<template>
  <div class="row mx-md-n5 gx-0 mt-2">
  <div class="col px-md-5">
    <table class="table table-bordered t-50">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Libelle</th>
      <th scope="col">Option</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="(item, index) in categories">
      <th>{{index+1}}</th>
      <td>{{item.libelle}}</td>
      <td>
        <button type="button" v-on:click="showModal(item)" class="btn btn-warning" >Modifier</button>
        <button type="button" v-on:click="deleteCategorie(item)" class="btn btn-danger m-1">Supprimer</button>
      </td>
    </tr>
  </tbody>
</table>
  </div>
  <div class="col px-md-5">
    <form class="form-inline" @submit.prevent="addCategorie">
      <div class="form-group">
        <label for="libelle">Libelle</label>
        <input type="text" class="form-control" id="libelle" v-model="categorie.libelle" placeholder="libelle...">
      </div>
      <button class="btn btn-primary mt-2" type="submit">Ajouter</button>
      <button type="reset" class="btn btn-danger m-1 mt-2">Annuler</button>
    </form>
  </div>
</div>
  <div class="modal" id="myModal">
    <div class="modal-dialog">
      <div class="modal-content">
      <div class="modal-header">
        <h1 class="h4 text-gray-900 mb-4">Modifier une catégorie</h1>
        <a v-on:click="CloseModal" class="btn btn-outline-secondary btn-circle btn-sm">
          <i class="fas fa-window-close"></i>
        </a>
      </div>
      <form @submit.prevent="updateCategorie">
        <div class="form-row m-3">
          <div class="col">
            <label for="libelle">Libelle</label>
            <input type="text" id="nom" name="nom" class="form-control" v-model="categorie.libelle" placeholder="libelle...">
          </div>
        </div>
        <button type="submit" class="btn btn-outline-primary m-4">Modifier</button>
        <button type="reset" class="btn btn-outline-danger m-2">Annuler</button>
      </form>
    </div>
    </div>
  </div>
</template>