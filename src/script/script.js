// 设置标题和卡片信息
// document.getElementById("mainTitle").innerText = "动态标题";
// document.getElementById("subtitle").innerText = "小标题";

$(document).ready(function () {
  $("#to_en").click(function (event) {
    event.preventDefault();
    $(".cn").addClass("hidden");
    $(".en").removeClass("hidden");
  });
  $("#to_cn").click(function (event) {
    event.preventDefault();
    $(".en").addClass("hidden");
    $(".cn").removeClass("hidden");
  });
});
