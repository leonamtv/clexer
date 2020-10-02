#!/bin/bash
if [ $# -eq 0 ]
  then
    python3 -m core.shell
else
    case "$1" in
    --test) 
        for file in ./samples/*.c
        do
            if [[ $file != *"__init__"* ]]; then
                echo "Testando $file"; echo ""
                python3 main.py "$file"
                printf -- '-%.0s' $(seq 100); echo ""
                echo "Teste com o arquivo $file rodado."
                printf -- '-%.0s' $(seq 100); echo ""
            fi
        done
        ;;
    --*) 
        printf -- '-%.0s' $(seq 100); echo ""
        echo "Atributo não reconhecido: $1"
        printf -- '-%.0s' $(seq 100); echo ""
        ;;
    *) 
        python3 main.py $@
        ;;
    esac
fi
exit 0