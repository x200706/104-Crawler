function deleteRowsWithKeyword() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getActiveSheet();
  var data = sheet.getDataRange().getValues();

  //清除第一欄以外的多餘表頭
  for (var i = data.length - 1; i >= 0; i--) {
    if (data[i][0] === "jobName") { // 這裡假設地區欄位是第一欄，如果是其他欄位，請修改[data[i][0]]中的0為欄位索引
      sheet.deleteRow(i + 1); // 刪除整列資料，索引+1是因為試算表索引從1開始，而陣列索引從0開始
    }
  }

  //地點清洗
  for (var i = data.length - 1; i >= 0; i--) {
    if (data[i][0] === "台北市士林區"||
        data[i][0] === "台北市內湖區"||
        data[i][0] === "台北市文山區"||
        data[i][0] === "台北市北投區"||
        data[i][0] === "新北市三峽區"||
        data[i][0] === "新北市五股區"||
        data[i][0] === "新北市永和區"||
        data[i][0] === "新北市汐止區"||
        data[i][0] === "新北市林口區"||
        data[i][0] === "新北市金山區"||
        data[i][0] === "新北市深坑區"||
        data[i][0] === "新北市新店區"||
        data[i][0] === "新北市新莊區"||
        data[i][0] === "新北市蘆洲區"||
        data[i][0] === "新北市鶯歌區"
    ) { // 這裡假設地區欄位是第一欄，如果是其他欄位，請修改[data[i][0]]中的0為欄位索引
      sheet.deleteRow(i + 1); // 刪除整列資料，索引+1是因為試算表索引從1開始，而陣列索引從0開始
    }
  }

  //職缺清洗
  for (var i = data.length - 1; i >= 0; i--) {
    if (data[i][0].indexOf("") !== -1) { // 檢查地區欄位是否包含關鍵字
      sheet.deleteRow(i + 1); // 刪除整列資料，索引+1是因為試算表索引從1開始，而陣列索引從0開始
    }
  }
}