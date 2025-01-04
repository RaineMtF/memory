import $ from "https://esm.sh/jquery";

// 设置标题和卡片信息
// document.getElementById("mainTitle").innerText = "动态标题";
// document.getElementById("subtitle").innerText = "小标题";

$(document).ready(function () {
  $("#to_eng").click(function (event) {
    event.preventDefault(); // 阻止链接的默认行为
    $(".nickname").text("Nickname");
    $(".datel").text("Departed");
    $(".dater").text("Born");
    $(".countdown").text("Countdown");
    $(".region").text("Location");
  });
  $("#to_chn").click(function (event) {
    event.preventDefault(); // 阻止链接的默认行为
    $(".nickname").text("昵称");
    $(".datel").text("逝世");
    $(".dater").text("出生");
    $(".countdown").text("倒计时");
    $(".region").text("地区");
  });
});