<script>

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
      <th scope="col">Image</th>
      <th scope="col">Catégorie</th>
      <th scope="col">Option</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>A</td>
      <td>A</td>
      <td>A</td>
      <td>A</td>
      <td>
        <button type="button" class="btn btn-warning">Modifier</button>
        <button type="button" class="btn btn-danger m-1">Supprimer</button>
      </td>
    </tr>
  </tbody>
</table>
  </div>
  <div class="col px-md-5">
    <form class="form-inline">
      <div class="form-group">
        <label for="libelle">Libelle</label>
        <input type="text" class="form-control" id="libelle">
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea class="form-control" id="message" name="message" rows="5"></textarea>
      </div>
      <div class="form-group">
        <label for="description">Image</label>
        <input type="file" class="form-control" id="description">
      </div>
      <div class="form-group mt-3">
        <label for="description">Catégorie</label>
        <select class="form-select" aria-label="Default select example">
          <option disabled value="">Veuillez sélectionner votre choix</option>
          <option>One</option>
          <option>Two</option>
          <option>Three</option>
        </select>
      </div>
      <button class="btn btn-primary mt-2" type="submit">Ajouter</button>
      <button type="reset" class="btn btn-danger m-1 mt-2">Annuler</button>
    </form>
  </div>
</div>
</template>