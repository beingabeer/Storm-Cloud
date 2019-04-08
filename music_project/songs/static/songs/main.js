var AlbumsListPage = {
    init: function() {
        this.$container = $('.albums-container');
        this.render();
        this.bindEvents();
    },

    render: function() {

    },

    bindEvents: function() {
        $('.btn-favorite', this.$container).on('click', function(e) {
            e.preventDefault();

            var self = $(this);
            var url = $(this).attr('href');
            $.getJSON(url, function(result) {
                if (result.success) {
                    $('fa-star', self).toggleClass('active');
                }
            });

            return false;
        });
    }
};

var SongsListPage = {
    init: function() {
        this.$container = $('.songs-container');
        this.render();
        this.bindEvents();
    },

    render: function() {

    },

    bindEvents: function() {
        $('.btn-favorite', this.$container).on('click', function(e) {
            e.preventDefault();

            var self = $(this);
            var url = $(this).attr('href');
            $.getJSON(url, function(result) {
                if (result.success) {
                    $('fa-star', self).toggleClass('active');
                    window.location('http://localhost:8000/songs/')
                }
            });

            return false;
        });
    }
};

$(document).ready(function() {
    AlbumsListPage.init();
    SongsListPage.init();
});



window.setTimeout(function() {
  $("#alert_message").fadeTo(500, 0).slideUp(500, function(){
    $(this).remove();
  });
}, 3000);
