// JS for colour change of elements in country field

let countrySelected = $("#id_default_country").val();
if (!countrySelected) {
  $("#id_default_country").css("color", "#f29188");
}
$("#id_default_country").change(function () {
  countrySelected = $(this).val();
  if (!countrySelected) {
    $(this).css("color", "#f29188");
  } else {
    $(this).css("color", "#262626");
  }
});
