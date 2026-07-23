# No AI slop

[English](README.md) | Español

Esta skill elimina más de 20 patrones de "AI slop" de tus textos y también puede ayudarte a detectarlos.

## Qué detecta

Los patrones que detecta incluyen:

| Patrón | Suena a |
|--------|---------|
| Contrastes binarios | "No es X. Es Y." |
| Aperturas que dan rodeos | "Seamos honestos..." |
| Falsos insights | "Lo que nadie te dice..." |
| Revelación con dos puntos | "Lo mejor de todo: aprende solo." |
| Análisis superficial | "...reflejando el compromiso del equipo" |
| Grandilocuencia | "marca un antes y un después" |
| Atribución vaga | "los expertos coinciden", "los estudios demuestran" |
| Verbos falsamente fuertes | "funge como un eje central" |
| Rotación de sinónimos | el agente, luego el asistente, luego la herramienta |
| Listado negativo | "No es un X. No es un Y. Es un Z." |
| Fragmentación dramática | "Eso es todo. Así de simple." |

También refuerza los fundamentos de la buena escritura: ir al punto cuando ayuda, usar voz activa, desenredar oraciones difíciles de seguir y preferir números concretos sobre abstracciones.

## Instalación

Pega esto en Claude Code, Codex o tu harness de AI favorito:

"Install this skill globally: [https://github.com/petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)"

## Uso

**1. Editar un borrador.** Pégalo e invoca la skill:

```
/no-ai-slop

[tu borrador]
```

Recibes el borrador editado más una sección breve de qué cambió. La skill hace la edición mínima efectiva y luego revisa su propio trabajo contra [eval.md](eval.md).

**2. Detectar slop.** Pregunta si un texto suena a AI:

```
/no-ai-slop is this AI slop?

[el texto]
```

Recibes cada patrón encontrado, cada uno con la línea citada.

## Archivos

1. `SKILL.md`: las reglas de edición y el flujo de trabajo.
2. `eval.md`: checks de pasa/falla que la skill corre sobre sus propias ediciones.

## Quién hizo esto

Esta es una skill de mi sistema operativo personal de AI. La biblioteca completa, incluyendo mis cursos y flujos de trabajo, vive en [Behind the Craft](https://behindthecraft.com).

## Licencia

MIT
