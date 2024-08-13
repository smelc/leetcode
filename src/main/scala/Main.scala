// Build with 'sbt compile'
// Run with 'sbt run'

@main def hello(): Unit =
  println("Hello world!")
  println(msg)

  val x = 3
  if x < 0 then
  println("negative")
  else if x == 0 then
  println("zero")
  else
  println("positive")

def msg = "I was compiled by Scala 3. :)"
