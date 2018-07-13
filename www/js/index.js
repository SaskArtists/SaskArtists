var artistsApp = new Vue({
  el: "#artists-app",
  data: {
    artists: [],
    search: ''
  },

  created:function() {
    this.loadArtists();
  },
  computed: {
    display: function() {
      this.search;
      var display = [];
      this.artists.forEach(function(artist){
          display.push(artist);
      });
      if(this.search == ""){
        return display;
      }
      else{
        return display.filter(searchForStart, this.search);
      }
    }
  },
  methods: {
    loadArtists: function() {
      var vm = this;
      var urlToGet = window.location.protocol + "//" + window.location.host + "/artists.json";
      axios.get(urlToGet)
        .then(function(response){
          vm.artists = response["data"];
        }).catch(function(response){
          console.log(response);
        });
    }
  }
});

function searchForStart(test){
  return test.name.toLowerCase().includes(this);
}
