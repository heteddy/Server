/**
 * Created by Elors on 2017/1/3.
 * Exercise-Group component
 */

define(['Exercise'], function () {

  Vue.component('exercise-group', {
    template: '\
      <div class="row store-row content-pane">\
        <el-form ref="form" :model="form" label-width="0px" class="page-pane">\
          <el-form-item label-width="0px"  class="text item-input"  v-show="shouldShow">\
            <el-input v-model="form.title" class="input" id="ex-title"></el-input>\
          </el-form-item>\
         <el-form-item label-width="0px"  class="text item-input"  v-show="shouldShow">\
            <el-input v-model="form.desc" class="input" id="ex-desc"></el-input>\
         </el-form-item>\
          <transition-group name="list" tag="div">\
            <store-exercise\
              v-for="(exercise, index) in form.exercises"\
              v-bind:list="form.exercises"\
              v-bind:exercise="exercise"\
              v-bind:index="index"\
              :key="index+\'ex\'">\
            </store-exercise>\
          </transition-group>\
          <el-form-item class="item-submit" v-show="shouldShow">\
            <el-button type="success" icon="plus" @click="onInsert">新增习题</el-button>\
            <el-button type="primary" icon="edit" @click="onSave">保存题组</el-button>\
          </el-form-item>\
        </el-form>\
      </div>\
    ',
    data: function () {
      return {
        form: {},
        shouldShow: false
      }
    },
    methods: {
      // Events Handle Method
      onInsert () {
        this.form.exercises.push(this.defaultExercise());
      },
      onSave () {
        let data = {'group': JSON.stringify(this.form)};
        console.log(data);
        malaAjaxPost('/lecturer/exercise/store', data, function(json) {
          if (json) {
            if (json.ok) {
              alert("操作成功");
              location.reload()
            } else {
              alert(json.msg);
            }
            return;
          }
          alert(DEFAULT_ERR_MSG);
        }, 'json', function(jqXHR, errorType, errorDesc) {
          let errMsg = errorDesc ? ('[' + errorDesc + '] ') : '';
          alert(errMsg + DEFAULT_ERR_MSG);
        });
      },
      // Public Method
      loadGroup (data) {
        let group = this;
        $.ajax({
          async: false,
          dataType: "json",
          url: '/lecturer/api/exercise/store?action=group&gid=' + data.id,
          success: function (json) {
            if (json && json.ok) {
              group.form = group.handleData(json.data);
              group.shouldShow = true;
            }
          }
        });
      },
      createGroup () {
        this.form = this.defaultGroup();
        this.shouldShow = true;
      },
      // Private Method
      handleData (json) {
        // format
        json.exercises = json.questions;
        delete json.questions;
        // set solution string
        for (exercise of json.exercises) {
          for (option of exercise.options) {
            if (exercise.solution === option.id) {
              exercise.solution = option.text;
            }
          }
        }
        return json
      },
      defaultGroup () {
        return {
          id: '',
          title: '题组名称',
          desc: '题组描述',
          exercises: [
            this.defaultExercise()
          ]
        }
      },
      defaultExercise () {
        return {
          id: '',
          title: '题目',
          solution: '选项1',
          analyse: '题目解析',
          options: [
            {
              id: '',
              text: '选项1'
            },
            {
              id: '',
              text: '选项2'
            },
            {
              id: '',
              text: '选项3'
            },
            {
              id: '',
              text: '选项4'
            }
          ]
        }
      }
    }
  });

});