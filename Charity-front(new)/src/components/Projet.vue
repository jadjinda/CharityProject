<script>
import axios from 'axios';
export default {
 data(){
   return {
    projet: {},
     categories: [],
     projets: []
  };
 },
  mounted() {
   this.listCategorie(),
       this.listProjet()
  },
  methods:{
   onImageChange(event){
     this.projet.image = event.target.files[0]
   },
    async listCategorie(){
     axios
          .get('http://127.0.0.1:5000/api/charity/listCategories')
          .then(value => {
            this.categories = value.data
            console.log(value.data)
          })
          .catch(error => {
            console.log(error)
          })
    },

    async listProjet(){
     axios
          .get('http://127.0.0.1:5000/api/charity/listProject')
          .then(value => {
            this.projets = value.data
            console.log(value.data)
          })
          .catch(error => {
            console.log(error)
          })
    },
    addProjet(){
     const formData = new FormData();
     formData.append('libelle', this.projet.libelle)
      formData.append('description', this.projet.description)
      formData.append('categorie_id', this.projet.categorie_id)
      formData.append('image', this.projet.image)
      axios.post('http://127.0.0.1:5000/api/charity/projects', formData,{
        headers:{'Contents-Type':'multipart/form-data'}
      }).then(response => {
        this.projet = {}
        this.listProjet()
      }).catch(error => {
        console.log('Error:', error);
      })
    },
    getUrlImage(monImage){
     return 'http://127.0.0.1:5000/charity/static/image/' + monImage
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
      <th scope="col">Description</th>
      <th scope="col">Catégorie</th>
      <th scope="col">Image</th>
      <th scope="col">Option</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="(item, index) in projets">
      <th>{{ index + 1}}</th>
      <td>{{ item.libelle }}</td>
      <td>{{ item.description }}</td>
      <td>{{ item.categorie }}</td>
      <td><img :src="getUrlImage(item.image)" :alt="item.libelle" width='50' height='20'></td>
      <td>
        <button type="button" class="btn btn-warning">Modifier</button>
        <button type="button" class="btn btn-danger m-1">Supprimer</button>
      </td>
    </tr>
  </tbody>
</table>
  </div>
  <div class="col px-md-5">
    <form class="form-inline" @submit.prevent="addProjet">
      <div class="form-group">
        <label for="libelle">Libelle</label>
        <input type="text" class="form-control" id="libelle" v-model="projet.libelle">
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea class="form-control" id="message" name="message" rows="5" v-model="projet.description"></textarea>
      </div>
      <div class="form-group">
        <label for="description">Image</label>
        <input type="file" class="form-control" id="description" @change="onImageChange" accept="image/*" required>
      </div>
      <div class="form-group mt-3">
        <label for="categorie">Catégorie</label>
        <select class="form-select" aria-label="Default select example" v-model="projet.categorie_id">
          <option v-for="categorie in categories" :key="categories.id" :value="categorie.id">
            {{ categorie.libelle }}</option>
        </select>
      </div>
      <button class="btn btn-primary mt-2" type="submit">Ajouter</button>
      <button type="reset" class="btn btn-danger m-1 mt-2">Annuler</button>
    </form>
  </div>
</div>
</template>