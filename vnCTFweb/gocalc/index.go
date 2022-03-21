package main

import (
	"embed"
	"fmt"
	"os"
	"reflect"
	"strings"
	"text/template"
	"github.com/gin-contrib/sessions"
	"github.com/gin-contrib/sessions/cookie"
	"github.com/gin-gonic/gin"
	"github.com/maja42/goval"
)

var tpl string

var source string

type Eval struct
{
	E string `json:"e" form:"e" binding:"required"`
}

func (e Eval) Result() (string, error)
{
	eval := goval.NewEvaluator() result, err := eval.Evaluate(e.E, nil, nil)
	if err != nil
	{
		return "", err
	}
	t := reflect.ValueOf(result).Type().Kind()
	if t == reflect.Int
	{
		return fmt.Sprintf("%d", result.(int)), nil
	}
	else if t == reflect.String
	{
		return result.(string), nil
	}
	else
	{
		return "", fmt.Errorf("not valid type")
	}
}

func (e Eval) String() string
{
	res, err := e.Result()
	if err != nil
	{
		fmt.Println(err) res = "invalid"
	}
	return fmt.Sprintf("%s = %s", e.E, res)
}

func render(c *gin.Context)
{
	session := sessions.Default(c)
	var his string
	if session.Get("history") == nil
	{
		his = ""
	}
	else
	{
		his = session.Get("history").(string)
	}
	fmt.Println(strings.ReplaceAll(tpl, "{{result}}", his))
	t, err := template.New("index").Parse(strings.ReplaceAll(tpl, "{{result}}", his))
	if err != nil
	{
		fmt.Println(err) c.String(500, "internal error")
		return
	} if err := t.Execute(c.Writer, map[string]string{ "s0uR3e": source, });
	err != nil { fmt.Println(err) }
}
func main() {
	port := os.Getenv("PORT")
}
if port == ""
{
	port = "8080"
}
r := gin.Default()
store := cookie.NewStore([]byte("woW_you-g0t_sourcE_co6e"))
r.Use(sessions.Sessions("session", store))
r.GET("/", func(c *gin.Context) { render(c) })
r.GET("/flag", func(c *gin.Context) {
	session := sessions.Default(c)
	session.Set("FLAG", os.Getenv("FLAG"))
	session.Save() c.String(200, "flag is in your session")
})
r.POST("/", func(c *gin.Context) {
	session := sessions.Default(c)
}
var his string
if session.Get("history") == nil
{
	his = ""
}
else
{
	his = session.Get("history").(string)
}
eval := Eval{}
if err := c.ShouldBind(&eval);
err == nil { his = his + eval.String() + ""
}
session.Set("history", his) session.Save() render(c)
})
r.Run(fmt.Sprintf(":%s", port)) } ] = invalid
