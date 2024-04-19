{
  "project" : "COLOCADORAS_FCI",
  "id" : "COLOCADORAS_FCI/MODIFICAR_TABLA",
  "lang" : "Shell",
  "description" : "",
  "type" : "Script",
  "properties" : "selectionScope: -2\nname: SCRIPT_MOD_LOT\ncaption: Solicitar modificar lotes negociables\ntype: display\ninputSchema:\n  type: object\n  title: Solicitar modificación en lotes negociables\n  hints:\n    fieldOrder:\n      - carga\n      - tasa\n      - plazo\n      - comentario\n  properties:\n    carga:\n      type: string\n      title: Cargar en el mercado?\n      enum:\n        - 'SI'\n        - ' NO'\n    tasa:\n      type: number\n      title: Tasa solicitada\n    plazo:\n      type: string\n      title: Plazo\n      enum:\n        - 'T+0'\n        - 'T+1'\n    comentario:\n      type: string\n      title: Comentario adicional\n\n",
  "env" : "",
  "form" : false
}