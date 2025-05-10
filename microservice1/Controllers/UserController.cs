using Microsoft.AspNetCore.Mvc;

[Route("api/[controller]")]
[ApiController]
public class UserController : ControllerBase
{
    private readonly AppDbContext _context;

    public UserController(AppDbContext context)
    {
        _context = context;
    }

    [HttpPost]
    public IActionResult Post([FromBody] UserData data)
    {
        if (string.IsNullOrWhiteSpace(data.Name) || !data.Email.Contains("@"))
        {
            return BadRequest("Invalid data");
        }

        _context.UserData.Add(data);
        _context.SaveChanges();
        return Ok(data);
    }
}
