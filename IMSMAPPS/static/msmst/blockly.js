
 //alert("ffff  ")
            function device(name,bg) {

  Blockly.Blocks[name] = {
  init: function() {

    this.appendDummyInput()
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField(new Blockly.FieldImage(bg, 115, 115, { alt: "*", flipRtl: "FALSE" }));
    this.appendStatementInput("NAME")
        .setCheck(null);
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
    this.appendDummyInput()
        .setAlign(Blockly.ALIGN_CENTRE)
        .appendField(new Blockly.FieldImage(bg, 115, 115, { alt: "*", flipRtl: "TRUE"}));
    this.setPreviousStatement(false, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

}          //    alert("{{ post.name }}");
  function microservice(name) {

Blockly.Blocks[name] = {
  init: function() {
    this.appendValueInput("NAME")
        .setAlign(Blockly.ALIGN_CENTRE)
        .appendField(name);
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};


}
  function data(name) {

  Blockly.Blocks[name] = {
  init: function() {
    this.appendStatementInput("NAME")
        .setCheck(null);

    this.setPreviousStatement(false, null);
    this.setNextStatement(false, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

}