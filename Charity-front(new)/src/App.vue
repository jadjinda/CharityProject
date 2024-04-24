<script setup>
import charity from "./assets/charity2.jpg"
import charity2 from "./assets/charity4.jpg"
import charity3 from "./assets/charity5.jpg"
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary fixed-top">
    <div class="container-fluid">
    <a class="navbar-brand" href="/">Charity</a>
    <div class="d-flex" id="navbarNavAltMarkup">
      <div class="navbar-nav m-2">
        <router-link to="/" class="nav-link active" aria-current="page">Acceuil</router-link>
        <router-link class="nav-link" to="/categorie">Nos Catégories</router-link>
        <router-link class="nav-link" to="/projet">Nos Projets</router-link>
        <a class="nav-link" href="#">Faire un don</a>
        <a class="nav-link" href="#">Nous Contacter</a>
      </div>
      <button type="button" class="btn btn-primary">Connexion</button>
    </div>
  </div>
  </nav>
  <div id="carouselExampleDark" class="carousel carousel-dark slide">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active" data-bs-interval="10000">
      <img :src="charity" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block text-white">
        <h5>BIENVENUE</h5>
        <p>Contribuer au développement des communautés en donnant pour des oeuvres de charité</p>
        <button type="button" class="btn btn-outline-light">Commencer</button>
      </div>
    </div>
    <div class="carousel-item" data-bs-interval="2000">
      <img :src="charity2" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block text-white">
        <h5>BIENVENUE</h5>
        <p>Contribuer au développement des communautés en donnant pour des oeuvres de charité</p>
        <button type="button" class="btn btn-outline-light">Commencer</button>
      </div>
    </div>
    <div class="carousel-item">
      <img :src="charity3" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block text-white">
        <h5>BIENVENUE</h5>
        <p>Contribuer au développement des communautés en donnant pour des oeuvres de charité</p>
        <button type="button" class="btn btn-outline-light">Commencer</button>
      </div>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
<router-view></router-view>
  <footer class="text-center bg-body-tertiary">
  <!-- Grid container -->
  <div class="container pt-4">
    <!-- Section: Social media -->
    <section class="mb-4">
      <!-- Facebook -->
      <a
        data-mdb-ripple-init
        class="btn btn-link btn-floating btn-lg text-body m-1"
        href="#"
        role="button"
        data-mdb-ripple-color="dark"
        ><i class="fab fa-facebook-f"></i
      ></a>

      <!-- Twitter -->
      <a
        data-mdb-ripple-init
        class="btn btn-link btn-floating btn-lg text-body m-1"
        href="#"
        role="button"
        data-mdb-ripple-color="dark"
        ><i class="fab fa-twitter"></i
      ></a>

      <!-- Google -->
      <a
        data-mdb-ripple-init
        class="btn btn-link btn-floating btn-lg text-body m-1"
        href="#"
        role="button"
        data-mdb-ripple-color="dark"
        ><i class="fab fa-google"></i
      ></a>

      <!-- Instagram -->
      <a
        data-mdb-ripple-init
        class="btn btn-link btn-floating btn-lg text-body m-1"
        href="#"
        role="button"
        data-mdb-ripple-color="dark"
        ><i class="fab fa-instagram"></i
      ></a>

      <!-- Linkedin -->
      <a
        data-mdb-ripple-init
        class="btn btn-link btn-floating btn-lg text-body m-1"
        href="#"
        role="button"
        data-mdb-ripple-color="dark"
        ><i class="fab fa-linkedin"></i
      ></a>
      <!-- Github -->
      <a
        data-mdb-ripple-init
        class="btn btn-link btn-floating btn-lg text-body m-1"
        href="#"
        role="button"
        data-mdb-ripple-color="dark"
        ><i class="fab fa-github"></i
      ></a>
    </section>
    <!-- Section: Social media -->
  </div>
  <!-- Grid container -->

  <!-- Copyright -->
  <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.05);">
    © 2024 Copyright:
    <a class="text-body" href="mailto:josueadjinda@gmail.com">josueadjinda08@gmail.com</a>
  </div>
  <!-- Copyright -->
</footer>
</template>

