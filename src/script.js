import $ from "https://esm.sh/jquery";

// 设置标题和卡片信息
// document.getElementById("mainTitle").innerText = "动态标题";
// document.getElementById("subtitle").innerText = "小标题";

$(document).ready(function () {
  $("#to_eng").click(function (event) {
    event.preventDefault();
    $(".chn").addClass("hidden");
    $(".eng").removeClass("hidden");
  });
  $("#to_chn").click(function (event) {
    event.preventDefault();
    $(".eng").addClass("hidden");
    $(".chn").removeClass("hidden");
  });
});