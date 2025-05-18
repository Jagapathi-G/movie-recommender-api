listen {
    port = 9117
  }

  namespace "nginx" {
    source_files = ["/logs/access.log"]

    format = "$remote_addr - $remote_user [$time_local] \"$request\" $status $body_bytes_sent \"$http_referer\" \"$http_user_agent\""

    labels {
      app = "fastapi-app"
    }

    histogram_buckets = [0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]
  }
