import scala.concurrent.duration._

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import io.gatling.jdbc.Predef._

class BlazeDemo extends Simulation {

	val httpProtocol = http
		.baseURL("http://blazedemo.com")

	val scn = scenario("BlazeDemo")
		.exec(http("request_0")
			.get("/"))

	setUp(
		scn.inject(
			rampUsers(100) over (60 seconds),
			constantUsersPerSec(100) during (60 seconds)
			)
		.protocols(httpProtocol)
	)
}