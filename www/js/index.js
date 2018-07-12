var artistsApp = new Vue({
  el: "#artists-app",
  data: {
    name: [],
    location: [],
    changelog: [],
  },

  created:function() {
    this.loadArtists();
  },

  methods: {
    loadArtists: function() {
      var urlToGet = window.location.protocol + "//" + window.location.host + "/artists.json";
      axios.get(urlToGet)
        .then(function(response){
          console.log(response["data"]);
        });
    }
  }
})
