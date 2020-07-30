<template>
  <div class="container">
    <h1>MY FAMILY</h1>

    <!-- таблица отображающая таблицу femily -->
    <b-button type="button"
      id="addMemberBtn"
      align-left
      v-b-modal.add-member-modal
      class="btn-success">Добавить</b-button>
<!--    <b-table striped hover :items="family" id="main_table"></b-table>-->
<!--    Рукописная таблица  -->
    <table class="table table-bordered">
      <thead class="thead-dark">
        <tr>
          <th>ID</th>
          <th>NAME</th>
          <th>AGE</th>
          <th></th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="(member, index) in family" :key="index">
            <td class="family-uid" scope="row">{{member.id}}</td>
            <td>{{member.name}}</td>
            <td>{{member.age}}</td>
            <td>
              <div class="btn-group">
<!--                кнопка запускает функции которая фиксирует две переменных-->
                <button class="btn btn-primary"
                        @click="fixChangeMember(member)"
                        v-b-modal.change-member-modal>Change</button>
                <button class="btn btn-outline-danger">Delete</button>
              </div>
            </td>
        </tr>
      </tbody>

      </table>

    <!-- модальное окно добавления члена семьи -->
    <b-modal ref="addMemberFamilyModal"
      id="add-member-modal"
      title="Добавить члена семьи"
      hide-footer>
      <b-form @submit="onSubmit" @reset="onReset"
      class="w-100">
      <b-form-group id="form-member-group"
        label="Введите данные"
        label-for="form-member-name-input">
      <!-- ввод имени -->
      <b-form-input id="form-member-name-input"
        type="text"
        v-model="addFamilyMember.name"
        required
        placeholder="Имя">
      </b-form-input>
      <!-- ввод возраста -->
      <b-form-input id="form-member-age-input"
        type="text"
        v-model="addFamilyMember.age"
        required
        placeholder="Возраст">
      </b-form-input>
      </b-form-group>
      <b-button-group id="add-member-btn"
        align-right d-block>
        <b-button type="submit" variant="primary">Добавить</b-button>

        <b-button type="reset" variant="danger">Сброс</b-button>
      </b-button-group>
      </b-form>
    </b-modal>

    <!--    Изменение - модальное окно-->
    <b-modal ref="changeMemberModal"
      id="change-member-modal"
      title="Изменить члена семьи"
      hide-footer>
      <b-form @submit="onUpdateMember"
        @reset="onResetChange"
        class="w-100">
        <b-form-group id="form-member-update-group"
          label="Измените данные"
          label-for="form-member-update-name-input">
          <b-form-input id="form-member-update-name-input"
          type="text"
          v-model="changeMember.name"
          required
          placeholder="Имя">
          </b-form-input>
          <b-form-input id="form-member-update-age-input"
                        type="text"
                        v-model="changeMember.age"
                        required
                        placeholder="Возраст">
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Изменить</b-button>
          <b-button type="reset" variant="danger">Сброс</b-button>
        </b-button-group>
      </b-form>

    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

const dataURL = 'http://localhost:8081/';
const postURL = 'http://localhost:8081/add/';

export default {
  name: 'Family',
  data() {
    return {
      family: [],
      addFamilyMember: {
        name: '',
        age: '',
      },
      changeMember: {
        id: 0,
        name: '',
        age: '',
      },
      saveChangeMember: {
        id: 0,
        name: '',
        age: '',

      },
    };
  },
  methods: {
    getFamily() {
      axios.get(dataURL)
        .then((response) => {
          this.family = response.data.Family;
          console.table(this.family);
        });
    },
    onSubmit(event) {
      event.preventDefault();
      this.$refs.addMemberFamilyModal.hide();
      const requestData = {
        name: this.addFamilyMember.name,
        age: this.addFamilyMember.age,
      };
      axios.post(postURL, requestData)
        .then(() => {
          this.getFamily();
          this.resetMemberForm();
        });
    },
    onReset(event) {
      event.preventDefault();
      // this.$refs.addMemberFamilyModal.hide();
      this.resetMemberForm();
    },
    onResetChange() {
      this.changeMember = this.saveChangeMember;
      console.log(this.saveChangeMember);
    },
    fixChangeMember(member) {
      this.changeMember = member;
      this.saveChangeMember = member;
    },
    onUpdateMember(event) {
      event.preventDefault();
      this.$refs.changeMemberModal.hide();
      const requestData = {
        id: this.changeMember.id,
        name: this.changeMember.name,
        age: this.changeMember.age,
      };
      const member = dataURL + requestData.id;
      axios.put(member, requestData)
        .then(() => {
          this.getFamily();
        });
      console.log(member);
    },
    resetMemberForm() {
      this.addFamilyMember.name = '';
      this.addFamilyMember.age = '';
    },
  },
  created() {
    console.log('we is created place');
    this.getFamily();
  },
};
</script>

<style scoped>
.container {
  /* background-color: black; */
  /* display: flex;
  flex-direction: column;
  justify-content
  : center; */
}
#addMemberBtn {
  display: block;
  margin-top: 3rem;
}
.table {
  margin-top: 1rem;
}
#form-member-age-input {
  margin-top: 0.5rem;
}
#add-member-btn {
  margin-top: 2rem;
}
</style>
