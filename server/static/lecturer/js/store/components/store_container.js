/**
 * Created by Elors on 2016/12/29.
 * Store-Container component
 */

define(['GroupList', 'ExerciseGroup'], function () {

  Vue.component('store-container', {
    template: '\
      <div class="row store-row">\
       <div class="col-sm-9 store-col">\
         <exercise-group class="store-content"/>\
       </div>\
       <div class="col-sm-3 store-col">\
         <store-group-list class="store-content"\
           v-on:selected="handleGroupSelect"\
           v-on:onCreate="createGroup"\
         />\
       </div>\
      </div>\
    ',
    mounted: function () {

    },
    methods: {
      handleGroupSelect (data) {
        console.debug('Selected Group ' + data.id);
        this.$children[0].loadGroup(data);
      },
      refreshGroupList () {
        this.$children[1].refresh_list();
      }
    }
  });

  // render DOM
  let root = new Vue({
    el: '#store-root'
  });

});