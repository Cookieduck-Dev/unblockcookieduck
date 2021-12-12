import cdub
import os
#cdub.config() options: "cookieduck", "betteralgebra", "simplecalculator"
cdub.config("cookieduck")
port = int(os.environ.get("PORT", 5000))
cdub.run(debug = False, host="0.0.0.0",port=port)
