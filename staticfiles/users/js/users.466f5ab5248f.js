document.addEventListener("DOMContentLoaded", () => {
  //add account_clubs for account
  document.querySelectorAll(".account_name").forEach((account) => {
    account.onclick = function () {
      const account_id = this.parentElement.id;
      const clubs_div = document.querySelector("#account_clubs_div");
      clubs_div.innerHTML = "";
      const request = new XMLHttpRequest();
      request.open("GET", `account_clubs/${account_id}`);
      request.onload = () => {
        const data = JSON.parse(request.responseText);
        if (request.status == 200) {
          const clubs_div = document.querySelector("#account_clubs_div");
          for (var i = 0; i < data.length; i++) {
            const p = document.createElement("p");
            p.innerHTML = data[i];
            clubs_div.append(p);
          }
        } else {
          alert("failed");
          console.log(data.errors);
        }
      };
      request.send();
    };
  });

  //add account_id to delete_account_form
  document.querySelectorAll(".delete").forEach((del_button) => {
    del_button.onclick = () => {
      const account_id = del_button.parentElement.parentElement.id;
      const delete_account_form = document.querySelector(
        "#delete_account_form"
      );
      delete_account_form.action = `account/${account_id}`;
    };
  });

  //add account_id to edit_account_form
  document.querySelectorAll(".edit").forEach((edit_button) => {
    edit_button.onclick = () => {
      const account_id = edit_button.parentElement.parentElement.id;
      const edit_account_form = document
        .querySelector("#edit_account_modal")
        .querySelector("form");
      edit_account_form.action = `edit_account/${account_id}`;
    };
  });

  // retrieve notes
  document.querySelectorAll(".notes").forEach((note) => {
    note.onclick = () => {
      const agent_id = note.dataset.id;
      const modal_txt = document.querySelector("#modal_note_text");
      modal_txt.innerHTML = "Enter Notes Here";
      const note_form = document
        .querySelector("#notes_modal")
        .querySelector("form");
      note_form.action = `notes/${agent_id}`;
      note_form.method = "POST";
      const request = new XMLHttpRequest();
      //const csrftoken = Cookies.get('csrftoken');
      request.open("GET", `get_notes/${agent_id}`);
      request.onload = () => {
        const data = JSON.parse(request.responseText);
        if (request.status == 200) {
          alert("Hi");
          const note = data[0].fields["note"];
          alert(note);
          modal_txt.innerHTML = note;
        } else {
          alert("data load fail");
          console.log(data.errors);
        }
      };
      const data = new FormData();
      data.append("agent_id", agent_id);
      //data.append("csrfmiddlewaretoken", csrftoken);
      request.send(data);
    };
  });
  /*     FETCH add_club
  const add_club_form = document.querySelector("#add_club_form");
  add_club_form.onsubmit = () => {
    let url = add_club_form.action
    //do fetch
    let formData = new FormData()
    formData.append('')
    fetch(url,)
    //return false
    return false;
    // close modal
  };
  */
  /////////////////////////////////

  // Activate tooltip for css
  $('[data-toggle="tooltip"]').tooltip();

  // Select/Deselect checkboxes
  var checkbox = $('table tbody input[type="checkbox"]');
  $("#selectAll").click(function () {
    if (this.checked) {
      checkbox.each(function () {
        this.checked = true;
      });
    } else {
      checkbox.each(function () {
        this.checked = false;
      });
    }
  });
  checkbox.click(function () {
    if (!this.checked) {
      $("#selectAll").prop("checked", false);
    }
  });
});
