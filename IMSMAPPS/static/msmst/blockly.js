
 alert("ffff  ")
            function device(name,bg) {

  Blockly.Blocks[name] = {
  init: function() {
    this.appendStatementInput("NAME")
        .setCheck(null);
    this.appendDummyInput()
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField(new Blockly.FieldImage(bg, 115, 115, { alt: "*", flipRtl: "FALSE" }));
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

}
        function component(name,bg) {

  Blockly.Blocks[name] = {
  init: function() {
    this.appendStatementInput("NAME")
        .setCheck(null);
    this.appendDummyInput()
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField(new Blockly.FieldImage(bg, 115, 115, { alt: "*", flipRtl: "FALSE" }));
    this.setPreviousStatement(false, null);
    this.setNextStatement(false, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

}          //    alert("{{ post.name }}");
