<template>
  <div class="home">
    <h1 class="title">Muambator</h1>
    <p class="subtitle">Rastreamento Correios, China Post, Aliexpress, Shopee, Gearbest nunca foi tão fácil e inteligente!</p>
    <img src="https://www.muambator.com.br/static/images/flecha/xflecha-happiest.png.pagespeed.ic.u0M3FKWcaY.png" height="200px" width="200px">
    <div id="search-code-div">
      <input type="text" id="tracking-code-input" placeholder="Digite aqui seu código de rastreio">
      <button id="search-code-btn">Pesquisar</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Homepage',
}

</script>


<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Poppins&family=Roboto:wght@100&display=swap');

.title {
  font-family: 'Poppins', sans-serif;
  font-size: 26px;
}

.subtitle {
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  
}
</style>
