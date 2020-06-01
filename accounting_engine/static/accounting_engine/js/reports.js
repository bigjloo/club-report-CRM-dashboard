document.addEventListener("DOMContentLoaded", () => {
  const tables = document.querySelectorAll("table");
  tables.forEach((table) => {
    const row_nets = table.getElementsByClassName("net");
    var sum = 0;
    for (var i = 0; i < row_nets.length; i++) {
      sum += parseInt(row_nets[i].innerHTML);
    }
    const row = table.insertRow();
    for (var i = 0; i < table.rows[0].cells.length; i++) {
      row.insertCell(i);
    }
    const cell_total = row.insertCell(5);
    const cell_sum = row.insertCell(6);
    cell_total.innerHTML = "<h4><strong>Total</strong><h4>";
    cell_sum.innerHTML = `<h4><strong>${sum}</strong><h4>`;
  });
});
